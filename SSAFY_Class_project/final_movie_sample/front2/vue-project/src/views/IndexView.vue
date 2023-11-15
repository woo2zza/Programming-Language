<template>
  <div>
    <div class="container-fluid">
      <!-- 기본 carousel -->
      <IndexMainCarousel />
    </div>
    <div>
      <!-- Top Rated Movies -->
      <div class="d-flex justify-content-center align-items-center mt-5">
        <h1>Top Rated Movies</h1>
      </div>
      <div class="container my-5">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 row-cols-xl-5 g-4">
          <div class="col" v-for="movie in movies" :key="movie.id">
            <MovieCard :movie="movie" :type="true" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import IndexMainCarousel from '@/components/IndexMainCarousel.vue'
import MovieCard from '@/components/movie/MovieCard.vue'
import { getTopRatedMovies } from '@/apis/movieApi'

const movies = ref([])

// Top Rated 영화 목록
const fetchMovie = () => {
  getTopRatedMovies()
    .then((response) => {
      movies.value = response.data.results
    })
    .catch((error) => {
      console.error(error)
    })
}
onMounted(() => {
  fetchMovie()
})
</script>

<style scoped>
</style>
