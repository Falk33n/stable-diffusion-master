<script
	module
	lang="ts"
>
	import {
		Accordion as AccordionPrimitive,
		type AccordionHeaderProps,
		type AccordionTriggerProps,
		type WithoutChild,
	} from 'bits-ui';

	export const Accordion = AccordionPrimitive.Root;
</script>

<script lang="ts">
	import { cn } from '$utils';
	import { ChevronDown } from 'lucide-svelte/icons';

	let {
		ref = $bindable(null),
		class: className,
		level = 3,
		children,
		...props
	}: WithoutChild<AccordionTriggerProps> & {
		level?: AccordionHeaderProps['level'];
	} = $props();
</script>

<AccordionPrimitive.Header
	{level}
	class="flex"
>
	<AccordionPrimitive.Trigger
		bind:ref
		class={cn(
			'flex flex-1 items-center justify-between py-4 text-sm font-medium transition-all hover:underline [&[data-state=open]>svg]:rotate-180',
			className,
		)}
		{...props}
	>
		{@render children?.()}
		<ChevronDown
			aria-hidden
			class="text-muted-foreground size-4 shrink-0 transition-transform duration-200"
		/>
	</AccordionPrimitive.Trigger>
</AccordionPrimitive.Header>
