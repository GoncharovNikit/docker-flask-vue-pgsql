<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <div class="users" v-if="content">
      <h3>
        Users in system:
        <div class="users-list">
          <p v-for="user in content">
            {{ user[0] }} - {{ user[1] }}
          </p>
        </div>
      </h3>
    </div>
  </div>
</template>

<script>
// import process from process

export default {
    data() {
        return {
            content: ''
        } 
    },
    methods: {
        loadJson() {
            fetch("http://localhost:3007/api_test").then((resp) => resp.json().then(
                (data) => {
                    console.log(data)
                    this.content = data
                }
            ))
            this.content = 'hello'
        }
    },
    mounted() {
        this.loadJson()
    }
}
</script>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
