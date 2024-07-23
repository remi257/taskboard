<script setup lang="ts">
import Task from '../models/task'

const props = defineProps({
  isHeader: Boolean,
  task: Task
})

function completeTask(task?: Task) {
  console.log('completingTask', task)
}
</script>

<template>
  <div class="task-padded" v-if="isHeader">
    <div></div>
    <p class="task-prop header">Name</p>
    <p class="task-prop header">Start Date</p>
    <p class="task-prop header">End Date</p>
    <p class="task-prop header">Subtasks</p>
  </div>
  <div class="task task-padded" v-else-if="task">
    <button class="tick-button" v-on:click="completeTask(task)"></button>
    <p class="task-prop">{{ task?.name || 'No name :(' }}</p>
    <p class="task-prop">{{ task?.dateStart?.toLocaleDateString() || 'No start date :(' }}</p>
    <p class="task-prop">{{ task?.dateEnd?.toLocaleDateString() || 'No end date :(' }}</p>
    <p class="task-prop">{{ task?.subtasks?.length || '0' }}</p>
  </div>
  <div v-else>
    <h3>No task</h3>
  </div>
  <!-- <h3>{{ task?.name || "No name :(" }}</h3> -->
</template>

<style scoped lang="scss">
.task-prop {
  width: 150px;
  display: inline-block;
  text-align: center;
  font-size: large;
}

.header {
  font-weight: bold;
}

.task {
  border: 1px solid #333333;
  border-radius: 6px;
  position: relative;

  /* Default shadow */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Light shadow initially */

  transition: box-shadow 0.3s ease;

  &:hover {
    /* Shadow effect on hover */
    box-shadow: 0 8px 16px rgba(54, 0, 68, 0.5); /* Darker, larger shadow on hover */
  }
}

.task-padded {
  padding: 3px 6px;
  margin: 3px 0px;
}

.tick-button {
  width: 18px;
  height: 18px;
  background: transparent;
  border: 2px solid #555555;
  border-radius: 2px;
  position: relative; /* Establish positioning context */
  overflow: hidden; /* Prevent overflow */
  transition: border-color 0.3s ease; /* Transition only border color */

  &:hover {
    border-color: #00bd7e; /* Change border color on hover */
    border-width: 2px; /* Increase border width on hover */
  }

  &:after {
    content: '✓'; /* Define the tick mark */
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -52%); /* Center the tick mark */
    font-size: 14px; /* Adjust size of the tick mark */
    font-weight: bold;
    color: transparent; /* Hide the tick mark initially */
    opacity: 0; /* Hide the tick mark initially */
    transition:
      opacity 0.3s ease,
      color 0.3s ease; /* Smooth transitions */
  }

  &:hover:after {
    color: #00bd7e; /* Change color of tick mark on hover */
    opacity: 1; /* Make tick mark visible */
  }
}
</style>
