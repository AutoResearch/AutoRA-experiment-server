import { initJsPsych } from "jspsych";
import jsPsychExternalHtml from '@jspsych/plugin-external-html';
import axios from "axios";
import "./style.css";

// in case the user refreshes the page or exits
window.addEventListener("beforeunload", function (e) {
	e.preventDefault();
	// incomplete_save();
	return;
});

// 
// @TODO: reimplement best practice with VITE_ env vars
// from autora cookiecutter
// const index = async () => {
//   if (process.env.NODE_ENV === 'development' && process.env.REACT_APP_devNoDb === 'True') {
//       await main(0, 0)
//       return
//   }
//   let prolificId = null
//   if (process.env.REACT_APP_useProlificId === 'True') {
//       const queryString = window.location.search;
//       const urlParams = new URLSearchParams(queryString);
//       prolificId = urlParams.get('PROLIFIC_PID');
//   }
//   let condition = await getCondition(db, 'autora', prolificId)
//   if (condition && (prolificId !== null || process.env.REACT_APP_useProlificId === 'False')) {
//       const observation = await main(condition[0], condition[1])
//       waitPage()
//       await setObservation(db, 'autora', condition[0], observation)
//       await setBackup(db, 'autora', condition[0], condition[1], observation)
//       endPage()
//   } else {
//       root.render(
//           <React.StrictMode>
//               <Error/>
//           </React.StrictMode>
//       );
//   }
// }
// await index()

// sample function that might be used to check if a participant has given
// consent to participate.
var check_consent = function() {
	if (document.getElementById('consent_checkbox').checked) {
		return true;
	}
	else {
		alert("If you wish to participate, you must check the box next to the statement 'I agree to participate in this study.'");
		return false;
	}
};

// declare the block.
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
		// @TODO: conditional prolific implementation
		// var interaction_data = jsPsych.data.getInteractionData();
		// jsPsych.data.get().addToLast({interactions: interaction_data.json()});
		//   redirect_success("{{workerId}}", "{{assignmentId}}", "{{hitId}}", "{{code_success}}");
	}
});

// execute the timeline
jsPsych.run(timeline);

// // Pass message from jsPsych to NivTurk
// function pass_message(msg) {
//   axios.post("/experiment",
//     msg, { headers: {
//         'Content-Type': 'application/json; charset=utf-8'
//       }}).then(function (response) {
//     console.log(response);
//   }).catch(function (error) {
//     console.log(error);
//   });
// }

// Save an incomplete dataset.
function incomplete_save() {
	axios.post("/incomplete_save",
		jsPsych.data.get().json(),
		{ headers: {
			'Content-Type': 'application/json; charset=utf-8'
		}}).then(function (response) {
		console.log(response);
	}).catch(function (error) {
		console.log(error);
	});
}

// // Successful completion of experiment: redirect with completion code.
// function redirect_success(workerId, assignmentId, hitId, code_success) {
//   // Concatenate metadata into complete URL (returned on success).
//   var url = "https://app.prolific.co/submissions/complete?cc=" + code_success;
//   $.ajax({
//     url: "/redirect_success",
//     method: 'POST',
//     data: JSON.stringify(jsPsych.data.get().json()),
//     contentType: "application/json; charset=utf-8",
//   }).done(function(data, textStatus, jqXHR) {
//     window.location.replace(url);
//   }).fail(function(error) {
//     window.location.replace(url);
//   });
// }

// // Unsuccessful completion of experiment: redirect with decoy code.
// function redirect_reject(workerId, assignmentId, hitId, code_reject) {
//   // Concatenate metadata into complete URL (returned on reject).
//   var url = "https://app.prolific.co/submissions/complete?cc=" + code_reject;
//   $.ajax({
//     url: "/redirect_reject",
//     method: 'POST',
//     data: JSON.stringify(jsPsych.data.get().json()),
//     contentType: "application/json; charset=utf-8",
//   }).done(function(data, textStatus, jqXHR) {
//     window.location.replace(url);
//   }).fail(function(error) {
//     window.location.replace(url);
//   });
// }

// // Unsuccessful completion of experiment: redirect to error page.
// function redirect_error(error) {
//   // error is the error number to redirect to.
//   var url = "/error/" + error;
//   $.ajax({
//     url: "/redirect_error",
//     method: 'POST',
//     data: JSON.stringify(jsPsych.data.get().json()),
//     contentType: "application/json; charset=utf-8",
//   }).done(function(data, textStatus, jqXHR) {
//     window.location.replace(url);
//   }).fail(function(error) {
//     window.location.replace(url);
//   });
//}