const loginComponent = {
    setup() {
        const phone = ref('09390444542')
        const form = ref();
        const code = ref('')
        const valid = ref(false)
        const isTokenSent = ref(false)
        const phoneRules = ref([
            v => !!v || 'Phone is required',
            v => v.startsWith('09') || 'Phone starts with 09xxx',
            v => v.length === 11 || 'Phone should be 11 numbers',
        ])

        const login = () => form.value?.validate().then(({valid: isValid}) => {
            if (isValid)
                fetch('/api/v1/auth/login', {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        phone_number: phone.value,
                        code: parseInt(code.value)
                    })
                })
                    .then(response => {
                        if (response.ok)
                            return response.json()
                        else
                            throw new Error(response)
                    })
                    .then(data => {
                        console.log("success", data)
                        if (!data['ok']) {
                            store.commit('showMessage', {text: data.message, color: 'error'})
                        }
                        if (!isTokenSent.value) {
                            isTokenSent.value = true;
                            store.commit('showMessage', {text: 'Token sent successfully!', color: 'green'})
                        } else {
                            if (data['access_token']) {
                                localStorage.setItem('access_token', data['access_token']);
                                router.push('/')
                            }
                        }
                    })
                    .catch(error => {
                        console.error(error)
                        store.commit('showMessage', {text: error, color: 'error'})
                    })
        })

        return {
            login,
            isTokenSent,
            code,
            form,
            phone,
            valid,
            phoneRules,
        };
    },
    template: `#login-template`,
}