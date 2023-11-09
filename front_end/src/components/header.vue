<template>
  <div>
    <div>
      <el-menu mode="horizontal" default-active="1" @select="handleSelect">
        <el-menu-item index="0">piapia</el-menu-item>
        <el-menu-item index="1">24</el-menu-item>
        <el-submenu index="2">
          <template slot="title">排行</template>
          <el-menu-item index="2-1">选项1</el-menu-item>
          <el-menu-item index="2-2">选项2</el-menu-item>
          <el-menu-item index="2-3">选项3</el-menu-item>
          <el-menu-item index="2-4">选项4</el-menu-item>
        </el-submenu>
        <el-avatar>匿名</el-avatar>
        <el-badge is-dot>
          <el-button size="small">签到</el-button>
        </el-badge>
        <el-button size="small">充值</el-button>
      </el-menu>
    </div>
    <div class="line"></div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>