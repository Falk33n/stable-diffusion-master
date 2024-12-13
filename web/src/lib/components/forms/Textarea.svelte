<script
	module
	lang="ts"
>
	export type FormTextareaEvent<T extends Event = Event> = T & {
		currentTarget: EventTarget & HTMLTextAreaElement;
	};

	export type TextareaEvents = {
		blur: FormTextareaEvent<FocusEvent>;
		change: FormTextareaEvent<Event>;
		click: FormTextareaEvent<MouseEvent>;
		focus: FormTextareaEvent<FocusEvent>;
		keydown: FormTextareaEvent<KeyboardEvent>;
		keypress: FormTextareaEvent<KeyboardEvent>;
		keyup: FormTextareaEvent<KeyboardEvent>;
		mouseover: FormTextareaEvent<MouseEvent>;
		mouseenter: FormTextareaEvent<MouseEvent>;
		mouseleave: FormTextareaEvent<MouseEvent>;
		paste: FormTextareaEvent<ClipboardEvent>;
		input: FormTextareaEvent<InputEvent>;
	};
</script>

<script lang="ts">
	import { cn } from '$utils';
	import type { WithElementRef, WithoutChildren } from 'bits-ui';
	import type { HTMLTextareaAttributes } from 'svelte/elements';

	let {
		ref = $bindable(null),
		value = $bindable(),
		class: className,
		...props
	}: WithoutChildren<WithElementRef<HTMLTextareaAttributes>> = $props();
</script>

<textarea
	bind:this={ref}
	bind:value
	class={cn(
		'border-input placeholder:text-muted-foreground focus-visible:ring-ring flex min-h-[60px] w-full resize-none rounded-md border bg-transparent px-3 py-2 text-sm shadow-sm focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-inset disabled:cursor-not-allowed disabled:opacity-50',
		className,
	)}
	{...props}
></textarea>
