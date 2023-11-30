import Vue from 'vue'
import Router from 'vue-router'
import home from '@/views/home'
import login from '@/views/auth/login'
import blackJack from '@/views/game/blackJack'
import gameIndex from '@/views/game'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
      children: [
        {
          path: '',
          component: gameIndex
        },
        {
          path: 'blackJack',
          component: blackJack
        }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/404',
      name: 'NotFound',
      component: () => import('@/views/error/404')
    },
    {
      path: '*',
      redirect: '/404'
    }
  ],
  mode: 'history'
})
router.beforeEach((to, from, next) => {
  if (to.fullPath == '/login') {
    next();
  } else {
    if (localStorage.getItem('name') == null) {
      next('/login');
    } else {
      next();
    }
  }
})
export default router
