<template>
  <div class="post-feed">
    <PostItem v-for="post in posts" :key="post.id" :post="post" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue'
import { fetchPosts } from '../services/mockApi'
import PostItem from '../components/PostItem.vue'
import type { Post } from '../model/post'

export default defineComponent({
  components: { PostItem },
  setup() {
    const posts = ref<Post[]>([])

    onMounted(async () => {
      posts.value = await fetchPosts()
    })

    return { posts }
  },
})
</script>

<style scoped>
.post-feed {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
</style>
