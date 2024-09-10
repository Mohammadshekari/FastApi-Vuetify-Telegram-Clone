const {vuex} = Vuex

const store = new Vuex.Store({
    state: {
        theme: 'light',
        drawer: false,
        snackbar: {
            text: '...',
            color: 'pink',
            show: false,
        },
        auth: {
            is_login: false,
        }
    },
    mutations: {
        setTheme(state, theme) {
            state.theme = theme
        },
        setDrawer(state, drawer) {
            state.drawer = drawer
        },
        showMessage(state, {text, color}) {
            console.log('showMessage', text, color)
            state.snackbar.text = text;
            state.snackbar.color = color;
            state.snackbar.show = true;
        },
        logout(state) {
            state.auth.is_login = false;
            localStorage.clear();
            router.push('/login');
        },
    }
})