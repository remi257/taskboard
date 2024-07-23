<script setup lang="ts">
import BoardItem from './BoardItem.vue'
import CreateTaskDialog from './CreateTaskDialog.vue'
import Task from '../models/task'
import { ref, reactive } from 'vue'
import { getService } from '@/services/servicefactory'
import { ITaskService } from '@/services/task/taskservice'

const tasksReady = ref(false)
const isDialogOpen = ref(false)
const tasks: Task[] = reactive([])
const apiMsg = ref('api not called')
const taskService = getService<ITaskService>(ITaskService)

getData()

function getData() {
  taskService.getTasks().then((data: Task[]) => {
    tasksReady.value = true
    tasks.length = 0
    tasks.push(...data)
  })
}

function openNewTaskDialog() {
  isDialogOpen.value = true
}

function handleFormSubmit(task: Task) {
  console.log('Form submitted:', task)
  taskService.createTask(task).then((t: Task) => tasks.push(t))
  // Handle form data here
}
</script>

<template>
  <div>Tasks</div>
  <div>{{ apiMsg }}</div>
  <button @click="openNewTaskDialog()">Add new</button>

  <div v-if="!tasksReady">Loading ...</div>
  <div v-else>
    <div v-if="tasks.length == 0">No tasks in db</div>
    <div v-else>
      <BoardItem :isHeader="true" />
      <BoardItem v-for="task in tasks" :task="task" />
    </div>
  </div>

  <CreateTaskDialog
    :isOpen="isDialogOpen"
    @close="isDialogOpen = false"
    @submit="handleFormSubmit"
  />
</template>

<style scoped></style>
