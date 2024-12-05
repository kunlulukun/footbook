<template>
  <div>
    <h1>Home Page</h1>
    <router-link to="/profile">Go to Profile</router-link>
    <CreatePost />
    <PostFeed />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import CreatePost from '../components/CreatePost.vue'
import PostFeed from '../components/PostFeed.vue'

export default defineComponent({
  name: 'HomePage',
  components: { CreatePost, PostFeed },
})
</script>
