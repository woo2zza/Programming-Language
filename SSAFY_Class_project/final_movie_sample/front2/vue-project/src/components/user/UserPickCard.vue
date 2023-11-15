<template>
  <div class="card h-100">
    <RouterLink :to="{ name: 'MovieDetailView', params: { moviePk: movie.id || movie.pk } }">
      <img :src="getImageUrl(movie.poster_path)" class="card-img-top" alt="..." />
      <div class="card-body text-center">
        <h5 class="card-title">{{ getFormattedTitle }}</h5>
      </div>
    </RouterLink>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  movie: Object
})

const getImageUrl = (path) => {
  // 이미지가 없는경우 예외처리
  if (!path) {
    return
  }
  return `https://image.tmdb.org/t/p/w500${path}`
}

const getFormattedTitle = computed(() => {
  const title = props.movie.title || props.movie.name
  return title.length > 15 ? title.slice(0, 15) + '...' : title
})
</script>

<style scoped>
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.card a,
.card a:hover {
  color: inherit;
  text-decoration: none;
}
</style>
