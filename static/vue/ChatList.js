app.component('ChatList', {
    setup() {
        const chats = [
            {id: 2, name: 'Patrick Star', lastMessage: 'Yo sponge bob! lets go to mr Crab 🦀', avatar: '/static/media/test/user-2.jpg'},
            {id: 3, name: 'BadiDesign Admin', lastMessage: 'Hi sir, Can you re-design telegram?💎', avatar: '/static/media/test/user-6.jpg'},
            {id: 4, name: 'Wall-E', lastMessage: 'Hi Mohammad, Whats up?', avatar: '/static/media/test/user-4.jpg'},
            {id: 5, name: 'Pro gamer', lastMessage: 'Hello', avatar: '/static/media/test/user-5.jpg'},
            {id: 1, name: 'Guitar Center', lastMessage: 'Hello', avatar: '/static/media/test/user-1.jpg'},
            {id: 6, name: 'Alireza', lastMessage: 'can you help me in Vue?', avatar: null},
            // Add more chats here
        ]
        return {
            chats,
        }
    },
    emits: ['chat-selected'],
    template: `
    <v-list class="py-0">
    <template 
        v-for="(chat,index) in chats"
        :key="chat.id">
      <v-list-item class="pa-2"
        :title="chat.name"
        @click="$emit('chat-selected', chat)"
      >
            <template v-slot:prepend>
                <v-avatar size="x-large">
                    <v-img :alt="chat.name" :src="chat.avatar ? chat.avatar : '/static/media/user.png'"></v-img>
                </v-avatar>
            </template>
            <template v-slot:subtitle>
                <div class="mt-1" v-html="chat.lastMessage"></div>
            </template>
      <template v-slot:append>
      <div class="d-flex flex-column justify-end text-right"> 
          <div class="text-caption pr-1 my-1">22:09</div>
            <v-badge
              color="green"
              content="6"
              inline
            ></v-badge>
        </div>
      </template>
      </v-list-item>
      <v-divider v-if="index !== chats.length - 1" inset></v-divider>
    </template>
      
    </v-list>
		`
})