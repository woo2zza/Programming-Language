<template>
    <MovieDetailInfo :movie="movie" />
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import MovieDetailInfo from '@/components/MovieDetailInfo.vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const movie = ref({});
const moviePK = route.params.moviePk;

const key = import.meta.env.VITE_TMDB_API_KEY;

const fetchMovieDetail = (moviePK) => {
  const movieUrl = `https://api.themoviedb.org/3/movie/${moviePK}?language=en-US&page=1`;
  const headers = {
    accept: 'application/json',
    Authorization: `Bearer ${key}`,
  };

  axios
    .get(movieUrl, { headers: headers })
    .then((response) => {
      movie.value = response.data;
    })
    .catch((error) => {
      alert('서버 에러');
      console.log(error);
    });
};


onMounted(() => {
  fetchMovieDetail(moviePK);
});
</script>

<style scoped>
</style>
