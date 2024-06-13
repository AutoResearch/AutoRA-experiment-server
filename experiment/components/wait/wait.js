customElements.define(
	'waiting-message',
	class WaitingMessage extends HTMLElement {
		constructor () {
			super();
			const template = document.getElementById('waiting-message');
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