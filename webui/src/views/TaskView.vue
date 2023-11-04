<template>
    <div class="container">
        <div class="main">
            <div class="btns">
                <el-button type="primary" @click="getTableData">刷新列表</el-button>
                <el-button type="primary" @click="sentAll">一键发送</el-button>
                <el-button type="danger" @click="deleteAll">清空任务</el-button>
            </div>
            <div class="table">
                <el-scrollbar height="85vh">
                    <el-table :data="tableData">
                        <el-table-column prop="id" label="学号"/>
                        <el-table-column prop="name" label="姓名"/>
                        <el-table-column prop="num" label="课程数"/>
                    </el-table>
                </el-scrollbar>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import request from '../utils/requests'

const tableData = ref([])
const getTableData = async () => {
    const res = await request({
        url: '/api/data',
        method: 'get'
    })
    tableData.value = res.data.data
    console.log(res.data)
}

const sent = async (key) => {
    const res = await request({
        url: '/api/sent/' + key,
        method: 'get'
    })
    console.log(res.data)
    console.log(key)
}

const deleteTask = async (key) => {
    const res = await request({
        url: '/api/delete/' + key,
        method: 'get'
    })
    console.log(res.data)
    console.log(key)
}

const sentAll = async () => {
    const res = await request({
        url: '/api/sentAll',
        method: 'get'
    })
    console.log(res.data)
}

const deleteAll = async () => {
    const res = await request({
        url: '/api/deleteAll',
        method: 'get'
    })
    console.log(res.data)
}

onMounted(() => {
    getTableData()
})
</script>

<style lang="less" scoped>
.container{
//   background-color: antiquewhite;
  flex: 1 1;
  .main{
    // background-color: rgb(221, 240, 240);
    padding: 25px;
    height: 100%;
    .btns{
        display: flex;
        justify-content: flex-end;
    }
  }
}
</style>