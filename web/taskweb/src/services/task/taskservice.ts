import type Task from "@/models/task";
import { type IService } from "../servicefactory";

export abstract class ITaskService implements IService {
	abstract getTasks(): Promise<Task[]>;
	abstract getTask(id: string): Promise<Task>;
	abstract completeTask(id: string): Promise<Task>;
	abstract createTask(task: Task): Promise<Task>;
}

export class TaskService implements ITaskService {
	async getTasks(): Promise<Task[]> {
		const response = await fetch('/api/tasks/get');
		const data = await response.json(); // Parse JSON response

		return data as Task[];
	}

	async getTask(id: string): Promise<Task> {
		const response = await fetch(`/api/tasks/get/${id}`);
		const data = await response.json(); // Parse JSON response

		return data as Task;
	}

	async completeTask(id: string): Promise<Task> {
		const response = await fetch(`/api/tasks/complete/${id}`);
		const data = await response.json(); // Parse JSON response

		return data as Task;
	}

	async createTask(task: Task): Promise<Task> {
		const response = await fetch(`/api/tasks/add`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(task)
		});
		const data = await response.json(); // Parse JSON response

		return data as Task;
	}

}

