app.component('Home', {
    setup() {
        const drawer = ref(false)
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

        return {
            drawer,
            group,
            items,
        }
    },
    template: '#home-template',

})