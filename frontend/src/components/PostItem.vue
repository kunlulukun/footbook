<template>
  <div class="post-item">
    <h3>{{ post.username }}</h3>
    <p>{{ post.content }}</p>
    <div class="actions">
      <span>{{ post.likes }} Likes</span>
      <button @click="likePost">Like</button>
    </div>
    <ul>
      <li v-for="(comment, index) in post.comments" :key="index">
        <strong>{{ comment.username }}</strong
        >: {{ comment.comment }}
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
import type { Post } from '../model/post'
import { defineComponent, type PropType } from 'vue'

export default defineComponent({
  props: {
    post: { type: Object as PropType<Post>, required: true },
  },
  methods: {
    likePost() {
      // eslint-disable-next-line vue/no-mutating-props
      this.post.likes++
    },
  },
})
</script>

<style scoped>
.post-item {
  border: 1px solid #ddd;
  padding: 16px;
  border-radius: 8px;
}
.actions {
  display: flex;
  justify-content: space-between;
}
</style>
