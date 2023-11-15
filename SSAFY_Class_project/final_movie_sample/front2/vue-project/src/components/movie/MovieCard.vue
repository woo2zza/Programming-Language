<template>
  <div class="card h-100 border-dark">
    <RouterLink :to="{ name: 'MovieDetailView', params: { moviePk: movie.id || movie.pk } }">
      <img :src="getImageUrl(movie.poster_path)" class="card-img-top" alt="..." />
      <div class="card-body text-center">
        <h5 class="card-title">{{ movie.title || movie.name }}</h5>
      </div>
    </RouterLink>
  </div>
</template>

<script setup>
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
</script>

<style scoped>

.card-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.card-title {
  margin-top: 1rem;
  font-size: 1.5rem;
  font-weight: bold;
}

.card img {
  height: 500px;
  object-fit: cover;
}

.card a,
.card a:hover {
  color: inherit;
  text-decoration: none;
}
</style>
