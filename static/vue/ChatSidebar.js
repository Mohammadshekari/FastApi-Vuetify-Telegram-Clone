app.component('ChatSidebar', {
    setup() {
        const chats = [
            {id: 1, name: 'Chat 1', lastMessage: 'Hello', avatar: 'path/to/avatar1.jpg'},
            {id: 2, name: 'Chat 2', lastMessage: 'How are you?', avatar: 'path/to/avatar2.jpg'},
            // Add more chats here
        ]
        return {
            chats,
        }
    },
    emits: ['chat-selected'],
    template: `
  <v-navigation-drawer app permanent>
    <v-list>
      <v-list-item
        v-for="chat in chats"
        :key="chat.id"
        @click="$emit('chat-selected', chat)"
      >
        <v-list-item-avatar>
          <v-img :src="chat.avatar"></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title>{{ chat.name }}</v-list-item-title>
          <v-list-item-subtitle>{{ chat.lastMessage }}</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
		`
})