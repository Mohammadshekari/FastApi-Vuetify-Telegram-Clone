app.component('ChatWindow', {
    props: {
        chat: Object,
    },
    setup() {
        const messages = ref([
            {id: 1, text: 'Hello', sent: true},
            {id: 2, text: 'Hi there!', sent: false},
            // Add more messages here
        ])
        return {
            messages,
        };
    },
    template: `
  <v-container>
    <v-list>
      <v-list-item
        v-for="message in messages"
        :key="message.id"
        :class="{ 'sent-message': message.sent }"
      >
        <v-list-item-content>
          <v-list-item-title>{{ message.text }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-container>
		`
})