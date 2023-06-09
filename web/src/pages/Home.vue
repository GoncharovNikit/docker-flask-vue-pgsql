<template>
    <div class="users" v-if="content">
        <h3>
            Users in system:
            <div class="users-list">
                <p v-for="user in content">{{ user[0] }} - {{ user[1] }}</p>
            </div>
        </h3>
    </div>
</template>

<script>
export default {
    data() {
        return {
            content: '',
        }
    },
    methods: {
        loadJson() {
            fetch('http://localhost:3007/api_test').then((resp) =>
                resp.json().then((data) => {
                    console.log(data)
                    this.content = data
                }),
            )
            this.content = 'hello'
        },
    },
    mounted() {
        this.loadJson()
    },
}
</script>

<style scoped>
.users {
    margin: 50px auto;
    width: 400px;
}
</style>
