<template>
  <div class="container mt-5">
    <div v-if="!userStore.isLogin" class="text-center">
      <p>게시글 작성을 위해선 로그인이 필요합니다.</p>
      <button class="btn btn-info mb-5" @click="redirectToLogin">로그인</button>
    </div>
    <div v-else>
      <div class="mb-3">
        <label for="rate" class="form-label">평점 </label>
        <select v-model="article.rate" class="form-select" style="width: auto">
          <option v-for="n in 10" :key="n" :value="n">{{ n }}</option>
        </select>
      </div>

      <div class="mb-3">
        <label for="title" class="form-label">제목</label>
        <input
          type="text"
          class="form-control"
          id="title"
          placeholder="게시판 제목"
          v-model="article.title"
          required
        />
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea
          class="form-control"
          v-model="article.content"
          placeholder="내 의견은..."
          rows="5"
          required
        ></textarea>
      </div>
      <button @click="submitArticle" class="btn btn-info mb-5">제출</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/userStore'
import { useArticleStore } from '@/stores/articleStore'

const route = useRoute()
const router = useRouter()

const userStore = useUserStore()
const articleStore = useArticleStore()

const moviePk = route.params.moviePk

const article = ref({
  rate: 5,
  title: '',
  content: ''
})

const redirectToLogin = () => {
  router.push({ name: 'userLogin' })
}

const submitArticle = () => {
  articleStore
    .addArticle(moviePk, article.value)
    .then(() => {
      article.value = {
        rate: 5,
        title: '',
        content: ''
      }
    })
    .catch((error) => {
      console.error(error)
    })
}
</script>

<style scoped></style>
