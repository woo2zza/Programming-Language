<template>
  <div class="card" style="width: 18rem;">
    <img :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" class="card-img-top" alt="Movie Poster">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <p class="card-text">{{ movie.overview }}</p>
      <button @click="goToDetail(movie.id)" class="btn btn-primary">Detail</button>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()
const goToDetail = function(moviePk) { 
  router.push(`/${moviePk}`) 
}


const movies = defineProps({
  movie: Object,
});
</script>

<style scoped>
.card {
  margin: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 1);
}

.card:hover {
  scale: 1.2;
  z-index: 1;

}

.card-img-top {
  object-fit: cover;
}

.card-title {
  font-size: 2rem;
  height: 90px;
}

.card-text {
  margin-bottom: 12px;
  text-overflow:ellipsis;
  word-break: break-word;
  overflow: hidden;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
}

.btn-primary {
  background-color: #007BFF;
  border-color: #007BFF;
}
</style>
