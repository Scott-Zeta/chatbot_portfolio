class Chatbox {
  constructor() {
    // Inject CSS
    const style = document.createElement('style');
    style.textContent = `
       body {
    font-family: 'Nunito', sans-serif;
    font-weight: 400;
    font-size: 100%;
    background: #F1F1F1;
}

*, html {
    --primaryGradient: linear-gradient(93.12deg, #581B98 0.52%, #9C1DE7 100%);
    --secondaryGradient: linear-gradient(268.91deg, #581B98 -2.14%, #9C1DE7 99.69%);
    --primaryBoxShadow: 0px 10px 15px rgba(0, 0, 0, 0.1);
    --secondaryBoxShadow: 0px -10px 15px rgba(0, 0, 0, 0.1);
    --primary: #581B98;
}

/* CHATBOX
=============== */
.chatbox {
    position: fixed;
    bottom: 30px;
    right: 30px;
}

/* CONTENT IS CLOSE */
.chatbox__support {
    display: flex;
    flex-direction: column;
    background: #eee;
    width: 300px;
    height: 350px;
    z-index: -123456;
    opacity: 0;
    transition: all .5s ease-in-out;
}

/* CONTENT ISOPEN */
.chatbox--active {
    transform: translateY(-40px);
    z-index: 123456;
    opacity: 1;

}

/* BUTTON */
.chatbox__button {
    text-align: right;
}

.send__button {
    padding: 6px;
    background: transparent;
    border: none;
    outline: none;
    cursor: pointer;
}


/* HEADER */
.chatbox__header {
    position: sticky;
    top: 0;
    background: orange;
}

/* MESSAGES */
.chatbox__messages {
    margin-top: auto;
    display: flex;
    overflow-y: scroll;
    flex-direction: column-reverse;
}

.messages__item {
    background: orange;
    max-width: 60.6%;
    width: fit-content;
}

.messages__item--operator {
    margin-left: auto;
}

.messages__item--visitor {
    margin-right: auto;
}

/* FOOTER */
.chatbox__footer {
    position: sticky;
    bottom: 0;
}

.chatbox__support {
    background: #f9f9f9;
    height: 450px;
    width: 350px;
    box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
}

/* HEADER */
.chatbox__header {
    background: var(--primaryGradient);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: 15px 20px;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    box-shadow: var(--primaryBoxShadow);
}

.chatbox__image--header {
    margin-right: 10px;
}

.chatbox__heading--header {
    font-size: 1.2rem;
    color: white;
}

.chatbox__description--header {
    font-size: .9rem;
    color: white;
}

/* Messages */
.chatbox__messages {
    padding: 0 20px;
}

.messages__item {
    margin-top: 10px;
    background: #E0E0E0;
    padding: 8px 12px;
    max-width: 70%;
}

.messages__item--visitor,
.messages__item--typing {
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
}

.messages__item--operator {
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
    border-bottom-left-radius: 20px;
    background: var(--primary);
    color: white;
}

/* FOOTER */
.chatbox__footer {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 20px 20px;
    background: var(--secondaryGradient);
    box-shadow: var(--secondaryBoxShadow);
    border-bottom-right-radius: 10px;
    border-bottom-left-radius: 10px;
    margin-top: 20px;
}

.chatbox__footer input {
    width: 80%;
    border: none;
    padding: 10px 10px;
    border-radius: 30px;
    text-align: left;
}

.chatbox__send--footer {
    color: white;
}

.chatbox__button button,
.chatbox__button button:focus,
.chatbox__button button:visited {
    padding: 10px;
    background: white;
    border: none;
    outline: none;
    border-top-left-radius: 50px;
    border-top-right-radius: 50px;
    border-bottom-left-radius: 50px;
    box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
}
      `;
    document.head.appendChild(style);

    // Create chatbox elements dynamically
    this.chatbox = document.createElement('div');
    this.chatbox.classList.add('chatbox');
    this.chatbox.innerHTML = `
        <!-- Paste your HTML structure here -->
        <div class="chatbox__support">
          <!-- Chatbox Header -->
          <div class="chatbox__header">
            <div class="chatbox__image--header">
              <img
                src="https://img.icons8.com/color/48/000000/circled-user-female-skin-type-5--v1.png"
                alt="User Avatar"
              />
            </div>
            <div class="chatbox__content--header">
              <h4 class="chatbox__heading--header">Chat Support</h4>
              <p class="chatbox__description--header">
                Hi. How can I help you?
              </p>
            </div>
          </div>
          <!-- Chatbox Messages -->
          <div class="chatbox__messages">
            <div></div>
          </div>
          <!-- Chatbox Footer -->
          <div class="chatbox__footer">
            <input type="text" placeholder="Write a message..." />
            <button class="chatbox__send--footer send__button">Send</button>
          </div>
        </div>
        <!-- Chatbox Toggle Button -->
        <div class="chatbox__button">
          <button>
            <img src="./assets/chatbox-icon.svg" alt="Chat Icon" />
          </button>
        </div>
      `;
    document.body.appendChild(this.chatbox);

    this.args = {
      openButton: this.chatbox.querySelector('.chatbox__button'),
      chatBox: this.chatbox.querySelector('.chatbox__support'),
      sendButton: this.chatbox.querySelector('.send__button'),
    };

    this.state = false;
    this.messages = [];
  }

  display() {
    const { openButton, chatBox, sendButton } = this.args;

    openButton.addEventListener('click', () => this.toggleState(chatBox));

    sendButton.addEventListener('click', () => this.onSendButton(chatBox));

    const node = chatBox.querySelector('input');
    node.addEventListener('keyup', ({ key }) => {
      if (key === 'Enter') {
        this.onSendButton(chatBox);
      }
    });
  }

  toggleState(chatbox) {
    this.state = !this.state;

    // Show or hide the box
    if (this.state) {
      chatbox.classList.add('chatbox--active');
    } else {
      chatbox.classList.remove('chatbox--active');
    }
  }

  onSendButton(chatbox) {
    var textField = chatbox.querySelector('input');
    let text1 = textField.value;
    if (text1 === '') {
      return;
    }

    let msg1 = { name: 'User', message: text1 };
    this.messages.push(msg1);

    fetch('https://chatbot-wxno.onrender.com/', {
      method: 'POST',
      body: JSON.stringify({ user_input: text1 }),
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((r) => r.json())
      .then((r) => {
        let msg2 = { name: 'bot', message: r };
        this.messages.push(msg2);
        this.updateChatText(chatbox);
        textField.value = '';
      })
      .catch((error) => {
        console.error('Error:', error);
        this.updateChatText(chatbox);
        textField.value = '';
      });
  }

  updateChatText(chatbox) {
    var html = '';
    this.messages
      .slice()
      .reverse()
      .forEach(function (item, index) {
        if (item.name === 'bot') {
          html +=
            '<div class="messages__item messages__item--visitor">' +
            item.message +
            '</div>';
        } else {
          html +=
            '<div class="messages__item messages__item--operator">' +
            item.message +
            '</div>';
        }
      });

    const chatmessage = chatbox.querySelector('.chatbox__messages');
    chatmessage.innerHTML = html;
  }
}

const chatbox = new Chatbox();
chatbox.display();
