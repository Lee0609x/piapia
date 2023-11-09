<template>
  <div>
    <commonHeader/>
    <el-button @click="logout">test</el-button>
    <el-button @click="test">test2</el-button>
    <commonFooter/>
  </div>
</template>

<script>
import commonHeader from '@/components/header.vue'
import commonFooter from '@/components/footer.vue'
export default {
  name: 'Home',
  components: {
    commonHeader,
    commonFooter
  },
  data () {
    return {
    }
  },
  methods: {
    logout() {
      this.$axios.get('/auth/logout').then(resp => {
        console.log(resp);
      })
    },
    test() {
      this.$axios.get('/auth/test').then(resp => {
        console.log('test fail')
      })
    }
  }
}
</script>
