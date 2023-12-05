<template>
    <div v-if="IsEmpty" class="d-flex flex-wrap justify-content-around">
     <MovieCard 
      v-for="movie in movies" 
      :key="movie.id"
      :movie="movie"/>  </div>

      <div v-else>
      <div class="buffering-container">
        <h1>로딩 중</h1>
        <div class="loader"></div>
      </div>
    </div>
</template>
   


<script setup>
import MovieCard from '@/components/MovieCard.vue';
import axios from 'axios';
import { ref, computed } from 'vue'
const key = import.meta.env.VITE_TMDB_API_KEY
const movies = ref([])

const options = {
  method: 'GET',
  url: 'https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1',
  params: { language : 'ko-KR', page:'1'},
  headers: {
    accept: 'application/json',
    Authorization: `Bearer ${key}`
  }
};



console.log(movies)
axios
.request(options)
.then(function (response) {
  movies.value=response.data.results;
})
.catch(function (error) {
  console.error(error);
});


const IsEmpty = computed(() => {
  return movies.value.length > 0 ? true : false
})
</script>

<style scoped>
.buffering-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.loader::before {
  content: "🌕 🌕 🌕";
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}


</style>