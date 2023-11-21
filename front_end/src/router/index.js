import Vue from 'vue'
import Router from 'vue-router'
import home from '@/views/home'
import login from '@/views/auth/login'

Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
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
