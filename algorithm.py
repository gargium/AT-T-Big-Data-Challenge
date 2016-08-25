import numpy
from scipy import stats
from flask import Flask, render_template, Markup, json
from bigData import bayArea

bayArea = bayArea()



# todo: fudge the data and say that the 2009 api scores were 2010 and onward so we have something for 2014


tractList = []
homeValues = []
incomeValues = []
APIValues = []

homeGrowthRates = []
incomeGrowthRates = []
APIGrowthRates = []

schoolList = []

numFac = 3

def APIValue(county):

    for i in range(2010, 2015):
        APIvalues.append(bayArea.get_api(county, i))

    for i in range(len(APIValues) - 1):
        APIGrowthRates.append(APIValues[i + 1] - APIValues[i])

    avgAPIGrowth = sum(APIGrowthRates) / (len(APIGrowthRates))

    sigmaAPI = numpy.std(APIGrowthRates)

    devAPI = APIGrowthRates[3] - avgAPIGrowth

    APIScoreFac = 0

    APIGrowth = np.array(APIGrowthRates)

    if (devAPI >= 3 * sigmaAPI):
        APIScoreFac = (1 / numFac)
    else:
        z = stats.zscore(APIGrowth)
        if (z > 0.5):
            APIScoreFac = (1 / numFac) * (z - 0.5) * 2
        else:
            APIScoreFac = -1 * (1 / numFac) * (z - 0.5) * 2

    # return APIScoreFac
    return 1


# get year over year growth rate
def BSI(county):

    tractList = bayArea.get_tracts(county)

    for key in tractList.items():
        for i in range(2010,2015):
            homeValues.append(bayArea.get_price(county, i, key))
            incomeValues.append(bayArea.get_income(county, i, key))

        for i in range(len(homeValues) - 1):
            homeGrowthRates.append(homeValues[i + 1] - homeValues[i])
            incomeValues.append(incomeValues[i + 1] - incomeValues[i])

        avgHomeValueGrowth = sum(homeGrowthRates) / (len(homeGrowthRates))
        avgIncomeGrowth = sum(incomeGrowthRates) / (len(incomeGrowthRates))

        sigmaHV = numpy.std(homeGrowthRates)
        sigmaIncome = numpy.std(incomeGrowthRates)

        devHV = homeGrowthRates[3] - avgHomeValueGrowth
        devIncome = incomeGrowthRates[3] - avgIncomeGrowth

        HVScoreFac = 0
        IncomeScoreFac = 0

        HVGrowth = np.array(homeGrowthRates)
        IncomeGrowth = np.array(incomeGrowthRates)

        if (devHV >= 3*sigmaHV):
            HVScoreFac = (1/numFac)
        else:
            z = stats.zscore(HVGrowth)
            if (z > 0.5):
                HVScoreFac = (1/numFac)*(z-0.5)*2
            else:
                HVScoreFac = -1*(1/numFac)*(z-0.5)*2

        if (devIncome >= 3 * sigmaIncome):
            IncomeScoreFac = (1 / numFac)
        else:
            z = stats.zscore(IncomeGrowth)
            if (z > 0.5):
                IncomeScoreFac = (1 / numFac) * (z - 0.5) * 2
            else:
                IncomeScoreFac = -1 * (1 / numFac) * (z - 0.5) * 2

        bsi = APIValue(county) + HVScoreFac + IncomeScoreFac

        # bayArea.set_bsi(county, key, bsi)

        print county + ": " + APIVALUE(count) + ", " + HVScoreFac + ", " + IncomeScoreFac


BSI("SF")
BSI("SR")
BSI("SC")

