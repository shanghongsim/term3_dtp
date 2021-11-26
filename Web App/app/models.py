
# class covid_deaths_prediction_model():
#     def __init__(self):
#         self.population_density = 0
#         self.gdp_per_capita = 0
#         self.stringency_index = 0
#         self.total_tests = 0
#         self.total_vaccinations = 0
#         self.reproduction_rate = 0
#         self.hosp_patients_per_million = 0
#         self.hosp_patients = 0
#         self.icu_patients_per_million = 0
#         self.icu_patients = 0
#         self.hospital_beds_per_thousand = 0

#     def calculate(self):
#         beta_values = [-2099.424138, -2222.174998, 3493.565565, 32060.81507, 58077.13723, -
#                        1801.516288, 1310.146048, -6206.185475, 27725.66157, 1588.219406, 4692.475045]
#         ypred = 0
#         x_values = [self.population_density, self.gdp_per_capita, self.stringency_index, self.total_tests, self.total_vaccinations, self.reproduction_rate,
#                     self.hosp_patients_per_million, self.hosp_patients, self.icu_patients_per_million, self.icu_patients, self.hospital_beds_per_thousand]
#         for i in range(len(beta_values)):
#             ypred += beta_values[i] * x_values[i]
#         return ypred
