<script
	module
	lang="ts"
>
	import {
		Tooltip as TooltipPrimitive,
		type TooltipContentProps,
	} from 'bits-ui';

	export const Tooltip = TooltipPrimitive.Root;
	export const TooltipTrigger = TooltipPrimitive.Trigger;
	export const TooltipProvider = TooltipPrimitive.Provider;
</script>

<script lang="ts">
	import { cn } from '$utils';

	let {
		ref = $bindable(null),
		class: className,
		sideOffset = 4,
		side = 'bottom',
		'aria-hidden': ariaHidden = true,
		...props
	}: TooltipContentProps = $props();
</script>

<TooltipPrimitive.Content
	bind:ref
	{sideOffset}
	{side}
	aria-hidden={ariaHidden}
	class={cn(
		'bg-primary text-primary-foreground animate-in fade-in-0 zoom-in-95 data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=closed]:zoom-out-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 z-50 overflow-hidden rounded-md px-3 py-1.5 text-xs',
		className,
	)}
	{...props}
/>
