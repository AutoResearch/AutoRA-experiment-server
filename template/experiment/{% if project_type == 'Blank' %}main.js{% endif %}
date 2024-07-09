import { initJsPsych } from "jspsych";
import jsPsychBrowserCheck from '@jspsych/plugin-browser-check';
import "./style.css";

// in case the user refreshes the page or closes the browser
window.addEventListener("beforeunload", function (e) {
	e.preventDefault();
	return;
});

var browserCheck = {
	type: jsPsychBrowserCheck,
	minimum_width: 1000,
	minimum_height: 600
};

// define the timeline
var timeline = [browserCheck];

// initialize jspsych
var jsPsych = initJsPsych({
	on_finish: function() {
		jsPsych.data.displayData();
	}
});

// start timeline
jsPsych.run(timeline);