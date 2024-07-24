app.component('DrawerPanel', {
    emits: ['toggleTheme', 'openDrawer'],
    setup() {
        const group = ref(null)
        const items = ref([
            {
                title: 'Foo',
                value: 'foo',
            },
            {
                title: 'Bar',
                value: 'bar',
            },
            {
                title: 'Fizz',
                value: 'fizz',
            },
            {
                title: 'Buzz',
                value: 'buzz',
            },
        ])

        const showAccounts = ref(true)

        function toggleShowAccount() {
            showAccounts.value = !showAccounts.value
        }

        function toggleTheme() {
            store.commit('setTheme', this.theme.value = this.theme.value === 'light' ? 'dark' : 'light')
        }

        function toggleDrawer() {
            console.log('WTF')
        }

        const myDrawer = ref(false)

        return {
            myDrawer,
            group,
            items,
            showAccounts,
            toggleShowAccount,
            toggleTheme,
            toggleDrawer,
        }
    },
    computed: {
        drawer() {
            return store.state.drawer
        },
        theme() {
            return store.state.theme
        },
    },
    watch: {
        drawer(newVale) {
            if (newVale !== this.myDrawer)
                this.myDrawer = newVale
        },
        myDrawer(newVale) {
            if (newVale !== this.drawer)
                store.commit('setDrawer', newVale)
        },
    },
    template: `<v-navigation-drawer  v-model="myDrawer" >
			<v-card class="rounded-0 bg-blue" variant="text">
				<v-card-text>
					<div class="d-flex justify-space-between">
						<v-avatar size="x-large">
							<v-img alt="John" src="/static/media/user.png"></v-img>
						</v-avatar>
						<v-btn variant="text"
							   :icon="theme !== 'light' ? 'mdi-wb-sunny' : 'mdi-nights-stay'"
							   @click="toggleTheme"
						></v-btn>
					</div>
				</v-card-text>
				<v-card-text class="pt-0 pb-2">
					<div class="d-flex justify-space-between">
						<div>
							<p class="text-white">
								Mohammad Shekari Badi
							</p>
							<p class="text-blue-lighten-5 text-caption mb-0 text-caption font-weight-light">
								+98 939 044 4542
							</p>
						</div>
						<div>
							<v-btn size="small"
								   :icon="showAccounts ? 'mdi-keyboard-arrow-up' : 'mdi-keyboard-arrow-down'"
								   color="white" variant="text" @click.prevent="toggleShowAccount()"></v-btn>
						</div>
					</div>
				</v-card-text>
			</v-card>
			<v-expand-transition>
				<div v-show="showAccounts">
					<v-card class="rounded-0 mt-2" variant="text" @click="">
						<v-card-text class="px-3 py-1 d-flex align-center">
							<v-badge color="green" class="mr-2 mb-1 account-checked-badge" location="bottom end">
								<v-avatar size="small">
									<v-img alt="John" src="/static/media/user.png"></v-img>
								</v-avatar>
								<template v-slot:badge>
									<v-icon icon="mdi-sharp mdi-check"></v-icon>
								</template>
							</v-badge>

							<span class="text-subtitle-caption">Mohammad Shekari Badi</span>
						</v-card-text>
					</v-card>
					<v-card class="rounded-0 mb-2" variant="text" @click="">
						<v-card-text class="px-3 py-1">
							<v-avatar size="small" class="mr-2">
								<v-icon color="grey" size="large" class="mb-1" icon="mdi-add"></v-icon>
							</v-avatar>
							<span class="text-subtitle-caption">Add Account</span>
						</v-card-text>
					</v-card>
					<v-divider></v-divider>
				</div>
			</v-expand-transition>

			<v-card class="rounded-0 my-1" variant="text" @click="">
				<v-card-text class="px-3 py-2">
					<div>
						<v-avatar size="small" class="mr-2">
							<v-icon color="grey" size="large" class="mb-1"
									icon="mdi-outlined mdi-account-circle"></v-icon>
						</v-avatar>
						<span class="text-subtitle-caption">My Profile</span>
					</div>
				</v-card-text>
			</v-card>
			<v-divider></v-divider>
			<v-card class="rounded-0 mt-1" variant="text" @click="">
				<v-card-text class="px-3 py-2">
					<div>
						<v-avatar size="small" class="mr-2">
							<v-icon color="grey" size="large" class="mb-1"
									icon="mdi-outlined mdi-bookmark"></v-icon>
						</v-avatar>
						<span class="text-subtitle-caption">Saved Messages</span>
					</div>
				</v-card-text>
			</v-card>
			<v-card class="rounded-0 mt-1" variant="text" @click="">
				<v-card-text class="px-3 py-2">
					<div>
						<v-avatar size="small" class="mr-2">
							<v-icon color="grey" size="large" class="mb-1"
									icon="mdi-outlined mdi-info"></v-icon>
						</v-avatar>
						<span class="text-subtitle-caption">Telegram Info</span>
					</div>
				</v-card-text>
			</v-card>
		</v-navigation-drawer>`,

})