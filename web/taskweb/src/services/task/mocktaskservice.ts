import type Task from "@/models/task";
import { ITaskService } from "./taskservice";

export class MockTaskService implements ITaskService {
	private tasks = new Map<string, Task>();

	constructor() {
		this.tasks.set(
			'AAAA',
			{
				name: 'Mock Task 1',
				dateStart: new Date("2024-07-10"),
				dateEnd: new Date("2024-07-20")
			}
		);
		this.tasks.set(
			'AAAB',
			{
				name: 'Mock Task 2',
				dateEnd: new Date("2024-07-25"),
				subtasks: [
					{
						name: 'subtask 2_1'
					},
					{
						name: 'subtask 2_2'
					}
				]
			}
		);
	}

	async getTasks(): Promise<Task[]> {
		return Array.from(this.tasks.values());
	}

	async getTask(id: string): Promise<Task> {
		return this.tasks.get(id)!;
	}

	async completeTask(id: string): Promise<Task> {
		const task = this.tasks.get(id)!;
		task.status = 'C';

		return task;
	}

	async createTask(task: Task): Promise<Task> {
		const newId = this.createId();
		this.tasks.set(newId, task);
		console.log('tasks', this.tasks);
		return task;
	}

	private currentId = [0, 0, 0, 2];
	private createId(): string {
		const newId = this.currentId.map(n => n < 30 ? String.fromCharCode(65 + n) : String.fromCharCode(48 + n))
		this.incrementCurrentId()
		return newId.join('');
	}

	private incrementCurrentId() {
		this.currentId[3]++;

		for (const i of [3, 2, 1]) {
			while (this.currentId[i] > 40) {
				this.currentId[i] -= 40;
				this.currentId[i - 1]++;
			}
		}
	}
}