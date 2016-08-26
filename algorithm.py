import numpy, scipy
from scipy import stats
from flask import Flask, render_template, Markup, json
from bigData import bayArea

bayArea = bayArea()

class algorithm:
    # get year over year growth rate
    def BSI(self, county):
        BSIDict = {}
        tractList = []
        homeValues = []
        incomeValues = []
        APIValues = []
        if (county=="SF"):
            APIValues = [787, 800, 800, 810, 815]
        elif(county=="SC"):
            APIValues = [806, 819, 831, 838, 849]
        elif(county=="SR"):
            APIValues = [792, 796, 803, 813, 822]

        homeGrowthRates = []
        incomeGrowthRates = []
        APIGrowthRates = []

        for i in range(len(APIValues) - 1):
            APIGrowthRates.append(100 * (float(APIValues[i + 1]) - float(APIValues[i])) / (float(APIValues[i])))

        avgAPIGrowth = sum(APIGrowthRates) / float((len(APIGrowthRates)))

        sigmaAPI = numpy.std(APIGrowthRates)

        devAPI = APIGrowthRates[-1] - avgAPIGrowth

        APIGrowth = numpy.array(APIGrowthRates)

        numFac = 3.0
        tractList = bayArea.get_tracts(county)
        for key in list(tractList.keys()):
            for i in range(2010,2015):
                dataPrice = bayArea.get_price(county, str(i), key)
                dataIncome = bayArea.get_income(county, str(i), key)
                if ((dataPrice != "No Price Data Available") and (dataIncome != "No Income Data Available")):
                    homeValues.append(float(dataPrice))
                    incomeValues.append(float(dataIncome))

            for i in range(len(homeValues) - 1):
                homeGrowthRates.append(100*(float(homeValues[i + 1]) - float(homeValues[i]))/(float(homeValues[i])))
                incomeGrowthRates.append(100*(float(incomeValues[i + 1]) - float(incomeValues[i]))/(float(incomeValues[i])))

            if ((len(homeGrowthRates) is not  0) and (len(incomeGrowthRates) is not 0)):
                avgHomeValueGrowth = sum(homeGrowthRates) / float((len(homeGrowthRates)))
                avgIncomeGrowth = sum(incomeGrowthRates) / float((len(incomeGrowthRates)))

                sigmaHV = numpy.std(homeGrowthRates)
                sigmaIncome = numpy.std(incomeGrowthRates)

                devHV = homeGrowthRates[-1] - avgHomeValueGrowth
                devIncome = incomeGrowthRates[-1] - avgIncomeGrowth

                HVScoreFac = 0.0
                IncomeScoreFac = 0.0
                APIScoreFac = 0.0

                HVGrowth = numpy.array(homeGrowthRates)
                IncomeGrowth = numpy.array(incomeGrowthRates)

                if (devHV >= 3*sigmaHV):
                    HVScoreFac = (1/numFac)
                else:
                    z_values = stats.zscore(HVGrowth)
                    p_values = scipy.stats.norm.sf(abs(z_values))
                    p = float(1 - p_values[-1])
                    z = float(z_values[-1])

                    if (z > 0):
                        HVScoreFac = (p/numFac)
                    else:
                        HVScoreFac = (-1*p/numFac)

                p = 0.0
                z = 0.0

                if (devIncome >= 3 * sigmaIncome):
                    IncomeScoreFac = float(1 / numFac)
                else:
                    z_values = stats.zscore(IncomeGrowth)
                    p_values = scipy.stats.norm.sf(abs(z_values))
                    p = float(1 - p_values[-1])
                    z = float(z_values[-1])
                    if (z > 0):
                        IncomeScoreFac = p/numFac
                    else:
                        IncomeScoreFac = (-1*p/numFac)

                p = 0.0
                z = 0.0

                if (devAPI >= 3 * sigmaAPI):
                    APIScoreFac = float(1 / numFac)
                else:
                    z_values = stats.zscore(APIGrowth)
                    p_values = scipy.stats.norm.sf(abs(z_values))
                    p = float(1 - p_values[-1])
                    z = float(z_values[-1])
                    if (z > 0):
                        APIScoreFac = p / numFac
                    else:
                        APIScoreFac = (-1 * p / numFac)


                # add call to compute API contribution to BSI
                bsi = HVScoreFac + IncomeScoreFac + APIScoreFac
                homeValues[:] = []
                incomeValues[:] = []
                APIValues[:] = []
                homeGrowthRates[:] = []
                incomeGrowthRates[:] = []
                APIGrowthRates[:] = []

                bayArea.set_bsi(county, key, bsi)
                BSIDict[key] = bsi
                
        return BSIDict;
