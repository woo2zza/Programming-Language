import { createRouter, createWebHistory } from 'vue-router'

// 프로필 페이지
import UserInfo from '@/components/user/UserInfo.vue'
import UserPick from '@/components/user/UserPick.vue'
import UserArticle from '@/components/user/UserArticle.vue'
import UserFollower from '@/components/user/UserFollower.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/IndexView.vue')
    },
    {
      path: '/user/login',
      name: 'userLogin',
      component: () => import('@/views/UserLoginView.vue')
    },
    {
      path: '/user/signup',
      name: 'userSignup',
      component: () => import('@/views/UserSignupView.vue')
    },
    {
      path: '/user/profile/:userId',
      name: 'userProfile',
      component: () => import('@/views/UserProfileView.vue'),
      beforeEnter: (to, from, next) => {
        const isCurrentUser = to.params.userId === window.localStorage.getItem('userPk')

        if (
          to.path.endsWith('info') ||
          to.path.endsWith('pick') ||
          to.path.endsWith('article') ||
          to.path.endsWith('follower')
        ) {
          next()
          return
        }

        next(
          isCurrentUser
            ? `/user/profile/${to.params.userId}/info`
            : `/user/profile/${to.params.userId}/pick`
        )
      },
      children: [
        { path: 'info', name: 'userInfo', component: UserInfo },
        { path: 'article', name: 'UserArticle', component: UserArticle },
        { path: 'pick', name: 'UserPick', component: UserPick },
        { path: 'follower', name: 'UserFollower', component: UserFollower }
      ]
    },

    {
      path: '/logout',
      name: 'logout',
      component: () => import('@/views/UserLogoutView.vue')
    },
    {
      path: '/movies',
      name: 'movies',
      component: () => import('@/views/MovieListView.vue')
    },
    {
      path: '/movies/recommended',
      name: 'recommended',
      component: () => import('@/views/RecommendedView.vue')
    },
    {
      path: '/movies/:moviePk',
      name: 'MovieDetailView',
      component: () => import('@/views/MovieDetailView.vue')
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('@/views/NotFoundView.vue')
    }
  ]
})

export default router
