import { initJsPsych } from "jspsych";
import jsPsychExternalHtml from '@jspsych/plugin-external-html';
import "./style.css";

// in case the user refreshes the page or closes the browser
window.addEventListener("beforeunload", function (e) {
	e.preventDefault();
	return;
});

// sample function that might be used to check if a participant has given consent to participate
var check_consent = function() {
	if (document.getElementById('consent_checkbox').checked) {
		return true;
	}
	else {
		alert("If you wish to participate, you must check the box next to the statement 'I agree to participate in this study.'");
		return false;
	}
};

var consent = {
	type: jsPsychExternalHtml,
	url: "components/consent.html",
	cont_btn: "start",
	check_fn: check_consent
};

// define the timeline
var timeline = [consent];

// initialize jspsych
var jsPsych = initJsPsych({
	on_finish: function() {
		jsPsych.data.displayData();
	}
});

// start timeline
jsPsych.run(timeline);