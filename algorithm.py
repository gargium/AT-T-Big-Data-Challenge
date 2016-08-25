import numpy
from scipy import stats

# todo: fudge the data and say that the 2009 api scores were 2010 and onward so we have something for 2014





homeValues = []
incomeValues = []
APIValues = [][]

homeGrowthRates = []
incomeGrowthRates = []
APIGrowthRates = []

numFac = 3;

# get year over year growth rate
def yearly_growth():
    for i in range (2010, 2015):
        homeValues.append(getHomeValue(i))
        incomeValues.append(getIncomeValue(i))
        APIValues.append(getAPIValue(i))

    for i in range(len(homeValues)-1):
        homeGrowthRates.append(homeValues[i+1] - homeValues[i])
        incomeValues.append(incomeValues[i+1] - incomeValues[i])

    for i in range(len(APIValues) -1):
        APIGrowthRates.append(APIValues[i+1] - APIValues[i])

    avgHomeValueGrowth = sum(homeGrowthRates) / (len(homeGrowthRates))
    avgAPIGrowth = sum(APIGrowthRates) / (len(APIGrowthRates))
    avgIncomeGrowth = sum(incomeGrowthRates) / (len(incomeGrowthRates))

    sigmaHV = numpy.std(homeGrowthRates)
    sigmaAPI = numpy.std(APIGrowthRates)
    sigmaIncome = numpy.std(incomeGrowthRates)

    devHV = homeGrowthRates[3] - avgHomeValueGrowth
    devAPI = APIGrowthRates[3] - avgAPIGrowth
    devIncome = incomeGrowthRates[3] - avgIncomeGrowth

    HVScoreFac = 1
    APIScoreFac =  1
    IncomeScoreFac = 1

    HVGrowth = np.array(homeGrowthRates)
    APIGrowth = np.array(APIGrowthRates)
    IncomeGrowth = np.array(incomeGrowthRates)

    if (devHV >= 3*sigmaHV):
        HVScoreFac = (1/numFac)
    else:
        z = stats.zscore(HVGrowth)
        if (z > 0.5):
            HVScoreFac = (1/numFac)*(z-0.5)*2
        else:
            HVScoreFac = -1*(1/numFac)*(z-0.5)*2

    if (devAPI >= 3 * sigmaAPI):
        APIScoreFac = (1 / numFac)
    else:
        z = stats.zscore(APIGrowth)
        if (z > 0.5):
            APIScoreFac = (1 / numFac) * (z - 0.5) * 2
        else:
            APIScoreFac = -1 * (1 / numFac) * (z - 0.5) * 2


    if (devIncome >= 3 * sigmaIncome):
        IncomeScoreFac = (1 / numFac)
    else:
        z = stats.zscore(IncomeGrowth)
        if (z > 0.5):
            IncomeScoreFac = (1 / numFac) * (z - 0.5) * 2
        else:
            IncomeScoreFac = -1 * (1 / numFac) * (z - 0.5) * 2

    return APIScoreFac + HVScoreFac + IncomeScoreFac
