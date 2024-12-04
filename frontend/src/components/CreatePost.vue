<template>
  <div class="create-post">
    <textarea v-model="content" placeholder="What's on your mind?" rows="3"></textarea>
    <button @click="submitPost">Post</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { createPost } from '../services/mockApi'
import type { Post } from '../model/post'

export default defineComponent({
  setup() {
    const content = ref('')

    const submitPost = async () => {
      if (content.value.trim()) {
        const newPost: Post = {
          id: Date.now(),
          userId: 1,
          username: 'You',
          content: content.value,
          likes: 0,
          comments: [],
        }
        await createPost(newPost)
        content.value = ''
        alert('Post created!')
      }
    }

    return { content, submitPost }
  },
})
</script>

<style scoped>
.create-post {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
</style>
