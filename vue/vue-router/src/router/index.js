import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserProfile from '@/components/UserProfile.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/user/:id',
      name: 'user',
      component: UserView,
      children: [
        {
          path: 'profile',
          name: 'profile',
          component: UserProfile
        },
        {
          path: 'post',
          name: 'post',
          component: UserPosts
        },
      ]
    }
  ],
})

router.beforeEach((to, from) => {
  const isAuthenticated = true

  if (!isAuthenticated && to.name !== 'about'){
    return {name: 'about'}
  }
})

export default router
