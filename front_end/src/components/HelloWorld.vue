<template>
  <div>
    <el-button >test</el-button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
    }
  },
  methods: {
    login() {
      this.$axios.get('/api/auth/logout').then(resp => {
        
      })
    }
  }
}
</script>
