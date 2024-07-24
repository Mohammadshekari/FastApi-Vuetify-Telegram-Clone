const {vuex} = Vuex

const store = new Vuex.Store({
    state: {
        theme: 'light',
        drawer: false,
    },
    mutations: {
        setTheme(state, theme) {
            state.theme = theme
        },
        setDrawer(state, drawer) {
            state.drawer = drawer
        },
    }
})