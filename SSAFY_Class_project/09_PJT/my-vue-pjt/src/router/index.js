import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movies',
      name: 'MovieListView',
      component: () => import('../views/MovieListView.vue')
    },
    {
      path: '/:moviePk',
      name: 'MovieDetailView',
      component: () => import('../views/MovieDetailView.vue')
    },
    {
      path: '/review-search',
      name: 'ReviewSearchView',
      component: () => import('../views/ReviewSearchView.vue')
    },
    {
      path: '/recommended',
      name: 'recommended',
      component: () => import('../views/RecommendedView.vue')
    }
  ]
})

export default router
