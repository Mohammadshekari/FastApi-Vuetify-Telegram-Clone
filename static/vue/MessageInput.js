app.component('MessageInput', {
    props: {
        chat: Object,
    },
    setup() {
        const message = ref('')
        const sendMessage = () => {
            if (this.message.trim() !== '') {
                this.$emit('send-message', this.message);
                this.message = '';
            }
        }
        return {
            message,
            sendMessage,
        };
    },
    template: `
<v-text-field
    v-model="message"
    append-icon="mdi-send"
    @click:append="sendMessage"
    label="Type a message"
    single-line
    clearable
  ></v-text-field>
		`
})