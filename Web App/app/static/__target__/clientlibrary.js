// Transcrypt'ed from Python, 2021-11-26 16:29:56
var time = {};
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import * as __module_time__ from './time.js';
__nest__ (time, '', __module_time__);
var __name__ = '__main__';
export var run_covid_deaths_prediction_model = function () {
	var beta_values = [50357.17171379, -(2336.25690542), -(2173.53831279), 2495.90837776, 35646.25020873, 52853.27470739, -(1728.53875944), 2419.7059956, -(10633.38913396), 42905.57244269, 4889.5741786, -(1037.0547739), 4066.43250911, -(488.18591709), -(11935.57046358), -(948.57385445), -(2674.09092253)];
	var population_density = float_validate (document.getElementById ('x1').value);
	var gdp_per_capita = float_validate (document.getElementById ('x2').value);
	var stringency_index = float_validate (document.getElementById ('x3').value);
	var total_tests = float_validate (document.getElementById ('x4').value);
	var total_vaccinations = float_validate (document.getElementById ('x5').value);
	var reproduction_rate = float_validate (document.getElementById ('x6').value);
	var hospital_beds_per_thousand = float_validate (document.getElementById ('x7').value);
	var hosp_patients_per_million = float_validate (document.getElementById ('x8').value);
	var hosp_patients = float_validate (document.getElementById ('x8').value);
	var icu_patients_per_million = float_validate (document.getElementById ('x9').value);
	var ypred = 0;
	var x_values = [1, population_density, gdp_per_capita, stringency_index, total_tests, total_vaccinations, reproduction_rate, hospital_beds_per_thousand, hosp_patients_per_million, hosp_patients, icu_patients_per_million, Math.pow (hosp_patients_per_million, 2), Math.pow (hosp_patients_per_million, 3), Math.pow (hosp_patients, 2), Math.pow (hosp_patients, 3), Math.pow (icu_patients_per_million, 2), Math.pow (icu_patients_per_million, 3)];
	for (var i = 0; i < len (beta_values); i++) {
		ypred += float (beta_values [i]) * float (x_values [i]);
	}
	document.getElementById ('ypred').value = str (ypred);
	return null;
};
export var run_gold_prices_prediction_model = function () {
	var beta_values = [167.59532555, 3.27480948, 6.15421778, 3.88627622, -(1.50507384), -(0.83803454), -(1.93104515), -(1.48844009), -(2.25722964), 2.92575393, -(9.09312879), 2.24138987];
	var new_deaths = float_validate (document.getElementById ('x1').value);
	var new_cases = float_validate (document.getElementById ('x2').value);
	var stringency_index = float_validate (document.getElementById ('x3').value);
	var total_tests = float_validate (document.getElementById ('x4').value);
	var total_vaccinations = float_validate (document.getElementById ('x5').value);
	var reproduction_rate = float_validate (document.getElementById ('x6').value);
	var hospital_beds_per_thousand = float_validate (document.getElementById ('x7').value);
	var hosp_patients_per_million = float_validate (document.getElementById ('x8').value);
	var hosp_patients = float_validate (document.getElementById ('x9').value);
	var icu_patients_per_million = float_validate (document.getElementById ('x10').value);
	var icu_patients = float_validate (document.getElementById ('x11').value);
	var ypred = 0;
	var x_values = [1, new_deaths, new_cases, stringency_index, total_tests, total_vaccinations, reproduction_rate, hospital_beds_per_thousand, hosp_patients_per_million, hosp_patients, icu_patients_per_million, icu_patients];
	for (var i = 0; i < len (beta_values); i++) {
		ypred += float (beta_values [i]) * float (x_values [i]);
	}
	document.getElementById ('ypred').value = str (ypred);
	return null;
};
export var float_validate = function (val) {
	if (val != null) {
		return float (val);
	}
	else {
		return float (0);
	}
};

//# sourceMappingURL=clientlibrary.map