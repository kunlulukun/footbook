<template>
  <div class="login-page">
    <h2>Login</h2>
    <input v-model="username" placeholder="Username" />
    <input v-model="password" type="password" placeholder="Password" />
    <button @click="login">Login</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'LoginPage',
  setup() {
    const username = ref('')
    const password = ref('')
    const router = useRouter()

    const login = () => {
      if (username.value && password.value) {
        alert('Logged in!')
        router.push('/home')
      } else {
        alert('Please fill out all fields.')
      }
    }

    return { username, password, login }
  },
})
</script>

<style scoped>
.login-page {
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 300px;
  margin: 50px auto;
}
</style>
