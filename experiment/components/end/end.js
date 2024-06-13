/**
 * This is the end page that is shown after the experiment
 */
customElements.define(
	'end-message',
	class EndMessage extends HTMLElement {
		constructor () {
			super();
			const template = document.getElementById('end-message');
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