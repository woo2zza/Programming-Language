<template>
  <div class="container">
    <div class="row row-cols-md-2 row-cols-lg-3 g-4">
      <div v-for="movie in movies" :key="index" class="col">
        {{ movie }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const key = import.meta.env.VITE_TMDB_API_KEY

const movies = ref([])
const url = 'https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=1'
    
axios.get(url)
  .then((response) => {
    movies.value = response.data.results
  })
  .catch((err) => {
    alert('Axios Error: ' + err.message)
  })

const movieIsEmpty = computed(() => {
  return movies.value.length > 0 ? true : false
})
onMounted(fetchMovie)
----------------------------------
import axios from 'axios';

const options = {
  method: 'GET',
  url: 'https://api.themoviedb.org/3/movie/top_rated',
  params: {language: 'en-US', page: '1'},
  headers: {
    accept: 'application/json',
    Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjM2Y1MWY5YjhjNjE5YzNiYTBiMmZmNmYzYzQwYjE3MCIsInN1YiI6IjY1NGQ4MGM4NjdiNjEzMDEwMmUyNjk3MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.K8_hrh5Al83peolzU6uMtOw897mgrC0HJkmQvcGou-k'
  }
};

axios
  .request(options)
  .then(function (response) {
    console.log(response.data);
  })
  .catch(function (error) {
    console.error(error);
  });



</script>
