<template>
  <div class="card h-100 border-dark">
    <RouterLink
      :to="{ name: 'MovieDetailView', params: { moviePk: article.movie.id || article.movie.pk } }"
    >
      <img :src="getImageUrl(article.movie.poster_path)" class="card-img-top" alt="..." />
      <div class="card-body">
        <h5 class="card-title">{{ getFormattedTitle }}</h5>
        <div class="card-content">
          <div>{{ formatContent(article.title) }}</div>
          <div>{{ article.rate }} / 10</div>
        </div>
      </div>
    </RouterLink>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  article: Object
})

const getImageUrl = (path) => {
  // 이미지가 없는경우 예외처리
  if (!path) {
    return
  }
  return `https://image.tmdb.org/t/p/w500${path}`
}

const getFormattedTitle = computed(() => {
  const title = props.article.movie.title || props.article.movie.name
  return title.length > 15 ? title.slice(0, 15) + '...' : title
})

const formatContent = (content) => {
  const cont = content.length > 13 ? content.slice(0, 13) + '...' : content
  return cont.replace(/\n/g, '<br />')
}
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}


.card-title {
  font-weight: bold;
  margin-bottom: 0.5rem;
  font-size: 1.5rem;
  text-align: center;
}
.card-content {
  display: flex;
  justify-content: space-between;
  font-weight: bold;
}

.card a,
.card a:hover {
  color: inherit;
  text-decoration: none;
}
</style>
