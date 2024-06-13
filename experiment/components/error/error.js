/**
 * This is the error page that is shown if there are no conditions in the database
 */
customElements.define(
	'error-message',
	class ErrorMessage extends HTMLElement {
		constructor () {
			super();
			const template = document.getElementById('error-message');
			const templateContent = template.content;
			const shadowRoot = this.attachShadow({mode: 'open'});
			shadowRoot.appendChild(templateContent.cloneNode(true));
		}

		// on append and move
		connectedCallback () {
			console.log('connected', this);
		}

		// on move and remove
		disconnectedCallback () {
			console.log('disconnected', this);
		}
	}
);