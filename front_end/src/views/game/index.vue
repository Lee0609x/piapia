<template>
  <div>
    <el-button type="primary" @click="blackJack">玩21点</el-button>
  </div>
</template>
<script>
import router from '@/router'
export default {
  methods: {
    blackJack() {
      router.push('blackJack');
    }
  }
}
</script>