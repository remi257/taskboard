export default class Task {
    name?: string;
    dateStart?: Date;
    dateEnd?: Date;
    subtasks?: Task[];
    status?: string;
}