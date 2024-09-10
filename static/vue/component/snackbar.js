app.component('snackbar', {
    template: `
<v-snackbar v-model="snackbar.show" location="top" :color="snackbar.color">
    {{ snackbar.text }}
    <template v-slot:actions>
        <v-btn variant="text" @click="snackbar = false">
            Close
        </v-btn>
    </template>
</v-snackbar>`,
    setup() {

    },
    computed: {
        snackbar() {
            return store.state.snackbar;
        },
    },
})
